import { readFileLines, determineInputFile } from './utils';

// https://adventofcode.com/2024/day/14

function mod(n: number, m: number): number {
    let result = n % m;
    return result < 0 ? result + m : result;
}

function getRobotPosition(robotPosition: number[]): number[] {
    const steps: number = 100;
    const newPosition: number[] = [];
    const [px, py, vx, vy] = robotPosition;
    newPosition[0] = mod(px + vx * steps, maxX);
    newPosition[1] = mod(py + vy * steps, maxY);
    return newPosition;
}

function countRobots(robots: number[][]): number {
    const midX: number = Math.floor(maxX / 2);
    const midY: number = Math.floor(maxY / 2);
    const quadrants: number[] = Array(4).fill(0);
    for (let robot of robots) {
        let [rx, ry] = robot;
        if (rx < midX && ry < midY) {           // Top left
            quadrants[0]++;
        } else if (rx > midX && ry < midY) {    // Top right
            quadrants[1]++;
        } else if (rx < midX && ry > midY) {    // Bottom left
            quadrants[2]++;
        } else if (rx > midX && ry > midY) {    // Bottom right
            quadrants[3]++;
        }
    }
    return quadrants.reduce((a, b) => a * b);
}

function solve(lines: string[]): void {
    const robots: number[][] = [];
    lines.forEach(line => {
        let [px, py, vx, vy] = Array.from(line.matchAll(/-?\d+/g), m => parseInt(m[0]));
        robots.push(getRobotPosition([px, py, vx, vy]));
    });
    console.log(countRobots(robots));
}

const maxX: number = 101;
const maxY: number = 103;
solve(readFileLines(determineInputFile()));
