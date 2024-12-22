import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/22

function encrypt(secret: number): number {
    let x = mix(secret, secret * 64);
    x = prune(x);
    x = mix(Math.floor(x / 32), x);
    x = prune(x);
    x = mix(x * 2048, x);
    x = prune(x);
    return x;
}

function mix(secret: number, n: number): number {
    return secret ^ n;
}

function mod(n: number, m: number): number {
    let result = n % m;
    return result < 0 ? result + m : result;
}

function prune(secret: number): number {
    return mod(secret, 16777216);
}

function solve(lines: string[]): void {
    let sequences: { [key: string]: number } = {};
    for (const line of lines) {
        let num = parseInt(line);
        let results: number[] = [num % 10];
        for (let i = 0; i < 2000; i++) {
            num = encrypt(num);
            results.push(num % 10);
        }
        let seen = new Set<string>();
        for (let i = 0; i < results.length - 4; i++) {
            let [a, b, c, d, e] = results.slice(i, i + 5);
            let seq = `${b - a},${c - b},${d - c},${e - d}`;
            if (seen.has(seq)) continue;
            seen.add(seq);
            if (!sequences.hasOwnProperty(seq)) sequences[seq] = 0;
            sequences[seq] += e;
        }
    };
    console.log('Sum:', Math.max(...Object.values(sequences)));
}

solve(readFileLines(determineInputFile()));
