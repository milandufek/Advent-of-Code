import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/9

function loadBlocks(diskPartition: string): string[] {
    let diskMap: string = diskPartition;
    let blocks: string[] = [];
    let id: number = 0;
    let count: number;
    let value: string;
    for (let i = 0; i < diskMap.length; i++) {
        count = Number(diskMap[i]);
        if (i % 2 === 0) {
            value = String(id);
            id++;
        } else {
            value = '.';
        }
        for (let j = 0; j < count; j++) {
            blocks.push(value);
        }
    }
    return blocks;
}

function solve(lines: string[]): void {
    const blocks: string[] = loadBlocks(lines[0]);
    let lastBlock: string;
    while (blocks.includes('.')) {
        lastBlock = blocks.pop() || '0';
        if (lastBlock === '.') {
            continue;
        }
        blocks[blocks.indexOf('.')] = lastBlock;
    }

    let checkSum: number = 0;
    for (let i = 0; i < blocks.length; i++) {
        checkSum += i * Number(blocks[i]);
    }
    console.log(checkSum);
}

solve(readFileLines(determineInputFile()));
