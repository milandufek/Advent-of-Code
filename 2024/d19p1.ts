import { readFileSync } from 'fs';
import { determineInputFile } from './utils';

// https://adventofcode.com/2024/day/19

function canFormDesign(patterns: string[], design: string): boolean {
    if (design === '') return true;
    for (let pattern of patterns) {
        if (design.startsWith(pattern)) {
            if (canFormDesign(patterns, design.slice(pattern.length))) {
                return true;
            }
        }
    }
    return false;
}

function solve(): void {
    let [first, second] = readFileSync(determineInputFile(), 'utf-8').split('\n\n');
    let patterns: string[] = first.trim().split(', ');
    let designs: string[] = second.trim().split('\n');
    let canMakeIt = designs.filter(design => canFormDesign(patterns, design)).length;
    console.log('Designs:', canMakeIt);
}

solve();
