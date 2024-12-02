import { readFileLines, determineInputFile, pairwise } from './utils';

// https://adventofcode.com/2024/day/2

function checkReport(report: number[]): Boolean {
    const results: Boolean[] = [];
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

    return results.every(Boolean);
}

function solve(lines: string[]): void {
    let count: number = 0;
    lines.forEach(line => {
        const report: number[] = line.split(' ').map(Number);
        if (checkReport(report)) {
            count++;
            return;
        }

        for (let i = 0; i < report.length; i++) {
            const reportCopy: number[] = [...report];
            reportCopy.splice(i, 1);
            if (checkReport(reportCopy)) {
                count++;
                break;
            }
        }
    });
    console.log('Count:', count);
}

solve(readFileLines(determineInputFile()));
