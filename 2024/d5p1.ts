import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/5

function solve(puzzleInput: string): void {
    const [rules, updates] = puzzleInput.split('\n\n');
    const preceding: Map<number, Set<number>> = new Map();

    rules.trim().split('\n')?.forEach((match) => {
        const [left, right] = match.split('|').map(Number);
        if (!preceding.has(right)) {
            preceding.set(right, new Set());
        }
        preceding.get(right)?.add(left);
    });

    function getScore(pages: number[]): number {
        const disallowed: Set<number> = new Set();
        for (const page of pages) {
            if (disallowed.has(page)) {
                return 0;
            }
            preceding.get(page)?.forEach((p) => disallowed.add(p));
        }
        return pages[Math.floor(pages.length / 2)];
    }

    let total = 0;
    updates.trim().split('\n').forEach((line) => {
        const pages = line.split(',').map(Number);
        total += getScore(pages);
    });

    console.log('Score:', total);
}

solve(readFileSync(determineInputFile(), 'utf-8'));
