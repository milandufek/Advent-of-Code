import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/3

function decode(memory: string): number {
    let sum: number = 0;
    const correctedMemory: string[] = Array.from(memory
        .matchAll(/mul\(\d+,\d+\)/g), match => match[0]);
    correctedMemory.forEach((item: string) => {
        const [a, b]: number[] = item.slice(4, -1).split(',').map(Number);
        sum += a * b;
    });
    return sum;
}

console.log('Sum:', decode(readFileSync(determineInputFile(), 'utf-8')));
