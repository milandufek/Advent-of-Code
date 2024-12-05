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

    function getScore(pages: number[], isReordered = false): number {
        const disallowedAfter: { [key: number]: number } = {};
        for (let i = 0; i < pages.length; i++) {
            const page: number = pages[i];
            if (disallowedAfter[page] !== undefined) {
                const j = disallowedAfter[page];
                const reordered = [...pages.slice(0, j), page, ...pages.slice(j, i), ...pages.slice(i + 1)];
                return getScore(reordered, true);
            }
            if (preceding.has(page)) {
                for (const p of preceding.get(page)!) {
                    if (disallowedAfter[p] === undefined) {
                        disallowedAfter[p] = i;
                    }
                }
            }
        }
        return isReordered ? pages[Math.floor(pages.length / 2)] : 0;
    }

    let total = 0;
    updates.trim().split('\n').forEach((line) => {
        const pages = line.split(',').map(Number);
        total += getScore(pages);
    });

    console.log('Score:', total);
}

solve(readFileSync(determineInputFile(), 'utf-8'));
