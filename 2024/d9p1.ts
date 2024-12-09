import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/9

function loadBlocks(diskPartition: string): number[] {
    let diskMap: number[] = diskPartition.split('').map(Number);
    let blocks: number[] = [];
    let id: number = 0;
    let value: number;
    for (let i = 0; i < diskMap.length; i++) {
        if (i % 2 === 0) {
            value = id;
            id++;
        } else {
            value = -1;
        }
        for (let j = 0; j < diskMap[i]; j++) {
            blocks.push(value);
        }
    }
    return blocks;
}

function solve(lines: string[]): void {
    const blocks: number[] = loadBlocks(lines[0]);
    let lastBlock: number;
    while (blocks.includes(-1)) {
        lastBlock = blocks.pop() || -1;
        if (lastBlock === -1) {
            continue;
        }
        blocks[blocks.indexOf(-1)] = lastBlock;
    }

    let checkSum: number = 0;
    for (let i = 0; i < blocks.length; i++) {
        checkSum += i * blocks[i];
    }
    console.log(checkSum);
}

solve(readFileLines(determineInputFile()));
