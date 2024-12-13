import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/13

function solve(lines: string): void {
    const inc: number = 10000000000000;
    let score: number = 0;
    for (const block of lines.split('\n\n')) {
        let [ax, ay, bx, by, px, py] = Array.from(block.matchAll(/\d+/g), m => parseInt(m[0]));
        if (bx === 0) {
            console.log('Error: bx is 0');
            return;
        }
        px += inc
        py += inc
        // https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        let ca: number = (px * by - py * bx) / (ax * by - ay * bx);
        let cb: number = (px - ax * ca) / bx;
        if (ca % 1 === 0 && cb % 1 === 0) {
            score += Number(ca * 3 + cb);
        }
    }
    console.log('Score:', score);
}

solve(readFileSync(determineInputFile(), 'utf-8'));
