import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/11

const cache = new Map<string, number>();

function count(stone: number, step: number): number {
    const key = `${stone},${step}`;
    if (cache.has(key)) return cache.get(key)!;
    if (step === 0)     return 1;
    if (stone === 0)    return count(1, step - 1);
    const ss = String(stone);
    const len = ss.length;
    let result: number;
    if (len % 2 === 0) {
        const left = ss.slice(0, len / 2);
        const right = ss.slice(len / 2);
        result = count(Number(left), step - 1) + count(Number(right), step - 1);
    } else {
        result = count(stone * 2024, step - 1);
    }
    cache.set(key, result);
    return result;
}

function solve(lines: string[], steps: number): void {
    const stones: number[] = lines[0].split(' ').map(Number);
    let total: number = 0;
    for (let stone of stones) total += count(stone, steps);
    console.log('Stones:', total);
}

solve(readFileLines(determineInputFile()), 75);
