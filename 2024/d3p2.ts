import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/3

function decode(memory: string): number {
    let sum: number = 0;
    const correctedMemory: string[] = Array.from(memory
        .matchAll(/(mul\(\d+,\d+\)|do\(\)|don\'t\(\))/g), match => match[0]);
    let operate: boolean = true;
    for (const item of correctedMemory) {
        if (item.startsWith('mul(') && operate) {
            const [a, b]: number[] = item.slice(4, -1).split(',').map(Number);
            sum += a * b;
        }
        else if (item === "do()")    operate = true;
        else if (item === "don't()") operate = false;
    }
    return sum;
}

console.log('Sum:', decode(readFileSync(determineInputFile(), 'utf-8')));
