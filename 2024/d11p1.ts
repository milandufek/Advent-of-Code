import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/11

function solve(lines: string[]): void {
    const repeat: number = 25;
    let stones: number[] = lines[0].split(' ').map(Number);
    for (let step = 0; step < repeat; step++) {
        let newOrder: number[] = [];
        for (let stone of stones) {
            if (stone === 0) {
                newOrder.push(1);
                continue;
            }
            const ss = String(stone)
            const len = ss.length;
            if (len % 2 === 0) {
                const left = ss.slice(0, len / 2);
                const right = ss.slice(len / 2);
                newOrder.push(Number(left));
                newOrder.push(Number(right));
            } else {
                newOrder.push(stone * 2024);
            }
            stones = newOrder;
        }
    }
    console.log('Stones:', stones.length);
}

solve(readFileLines(determineInputFile()));
