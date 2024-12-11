import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/8

function solve(lines: string[]): void {
    const grid = lines.map(line => line.trim());
    const rows = grid.length;
    const cols = grid[0].length;
    const antennas: { [key: string]: [number, number][] } = {};
    grid.forEach((row, r) => {
        row.split('').forEach((char, c) => {
            if (char !== '.') (antennas[char] ||= []).push([r, c]);
        });
    });

    const antinodes = new Set<string>();
    Object.values(antennas).forEach(a => {
        for (let i = 0; i < a.length; i++) {
            for (let j = i + 1; j < a.length; j++) {
                const [r1, c1] = a[i];
                const [r2, c2] = a[j];
                antinodes.add(`${2 * r1 - r2},${2 * c1 - c2}`);
                antinodes.add(`${2 * r2 - r1},${2 * c2 - c1}`);
            }
        }
    });

    const validAntinodes = Array.from(antinodes).filter(node => {
        const [r, c] = node.split(',').map(Number);
        return 0 <= r && r < rows && 0 <= c && c < cols;
    });
    console.log(validAntinodes.length);
}

solve(readFileLines(determineInputFile()));
