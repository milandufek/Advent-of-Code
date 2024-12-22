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
    let sum = 0;
    for (const line of lines) {
        let num = parseInt(line);
        for (let i = 0; i < 2000; i++) {
            num = encrypt(num);
        }
        sum += num;
    };
    console.log('Sum:', sum);
}

solve(readFileLines(determineInputFile()));
