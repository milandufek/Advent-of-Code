import { readFile, determineInputFile, pairwise } from './utils';

// https://adventofcode.com/2024/day/2


function solve(lines: string[]): void {
    let count: number = 0;
    lines.forEach(line => {
        const results: Boolean[] = [];
        const report: number[] = line.split(' ').map(Number);
        const steps: number[] = [1, 2, 3];
        const direction: string = report[0] > report[1] ? 'down' : 'up';

        pairwise(report).forEach(([a, b]) => {
            if (direction === 'down') {
                results.push(steps.includes(a - b));
            } else if (direction === 'up') {
                results.push(steps.includes(b - a));
            } else {
                results.push(false);
            }
        });

        if (results.every(Boolean)) { count++ }
    });
    console.log('Count:', count);
}

solve(readFile(determineInputFile()));
