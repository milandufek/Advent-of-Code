import { assert } from 'console';
import { readFileSync } from 'fs';

// https://adventofcode.com/2024/day/1

function readFileLines(path: string): string[] {
    const data: string = readFileSync(path, 'utf-8');
    return data.trim().split('\n').map(s => s.trim());
}

function solve(lines: string[]): void {
    const left: number[] = [];
    const right: number[] = [];
    lines.forEach(line => {
        const [a, b] = line.split('  ').map(Number);
        left.push(a);
        right.push(b);
    });
    assert (left.length === right.length);

    let score: number = 0;
    for (let i = 0; i < left.length; i++) {
        let count: number = right.filter(x => x === left[i]).length;
        score += left[i] * count;
    }
    console.log('Sum:', score);
}

solve(readFileLines('inputs/1.txt'));
