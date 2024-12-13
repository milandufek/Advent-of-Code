import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/13

function solve(lines: string): void {
    let score: number = 0;
    for (const block of lines.split('\n\n')) {
        let [ax, ay, bx, by, px, py] = Array.from(block.matchAll(/\d+/g), m => parseInt(m[0]));
        let minScore: number = Infinity;
        for (let a = 0; a < 100; a++) {
            for (let b = 0; b < 100; b++) {
                if (ax * a + bx * b === px && ay * a + by * b === py) {
                    minScore = Math.min(minScore, a * 3 + b);
                }
            }
        }
        if (minScore !== Infinity) {
            score += minScore;
        }
    }
    console.log('Score:', score);
}

solve(readFileSync(determineInputFile(), 'utf-8'));
