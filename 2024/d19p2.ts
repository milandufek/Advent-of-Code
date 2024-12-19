import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/19

function countCombinations(
    patterns: string[],
    design: string,
    cache: Map<string, number> = new Map()
): number {
    if (design === '') return 1;
    if (cache.has(design)) return cache.get(design)!;

    let count = 0;
    for (let pattern of patterns) {
        if (design.startsWith(pattern)) {
            count += countCombinations(patterns, design.slice(pattern.length), cache);
        }
    }

    cache.set(design, count);
    return count;
}

function solve(): void {
    let [first, second] = readFileSync(determineInputFile(), 'utf-8').split('\n\n');
    let patterns: string[] = first.trim().split(', ');
    let designs: string[] = second.trim().split('\n');
    let canMakeIt = designs.reduce((sum, design) => sum + countCombinations(patterns, design), 0);
    console.log('Designs:', canMakeIt);
}

solve();
