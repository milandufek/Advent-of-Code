package main

import (
	"bufio"
	"fmt"
	"os"
)

// Day 20: Donut Maze
// https://adventofcode.com/2019/day/20

type Point struct {
	R, C int
}

func getData(path string) []string {
	f, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer f.Close()

	var lines []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
	return lines
}

func isLetter(b byte) bool {
	return b >= 'A' && b <= 'Z'
}

func at(grid []string, r, c int) byte {
	if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[r]) {
		return ' '
	}
	return grid[r][c]
}

func parseDonut(grid []string) (map[Point]bool, map[string][]Point) {
	donut := map[Point]bool{}
	portals := map[string][]Point{}

	for r, line := range grid {
		for c := 0; c < len(line); c++ {
			ch := line[c]

			switch {
			case ch == '.':
				donut[Point{r, c}] = true

			case isLetter(ch):
				down := at(grid, r+1, c)
				right := at(grid, r, c+1)

				if isLetter(down) {
					name := string([]byte{ch, down})
					pos := Point{r - 1, c}
					if at(grid, r+2, c) == '.' {
						pos = Point{r + 2, c}
					}
					portals[name] = append(portals[name], pos)
				} else if isLetter(right) {
					name := string([]byte{ch, right})
					pos := Point{r, c - 1}
					if at(grid, r, c+2) == '.' {
						pos = Point{r, c + 2}
					}
					portals[name] = append(portals[name], pos)
				}
			}
		}
	}

	for name, positions := range portals {
		if len(positions) > 2 {
			panic(fmt.Sprintf("found a portal with more than 2 connections: %s", name))
		}
	}

	return donut, portals
}

func getPortalPairs(portals map[string][]Point) map[Point]Point {
	pairs := map[Point]Point{}
	for _, positions := range portals {
		if len(positions) == 2 {
			pairs[positions[0]] = positions[1]
			pairs[positions[1]] = positions[0]
		}
	}
	return pairs
}

var directions = []Point{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

type state1 struct {
	pos   Point
	steps int
}

func solve1(data []string) int {
	donut, portals := parseDonut(data)
	pairs := getPortalPairs(portals)
	start := portals["AA"][0]
	end := portals["ZZ"][0]

	queue := []state1{{start, 0}}
	visited := map[Point]bool{}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.pos == end {
			return cur.steps
		}

		for _, d := range directions {
			next := Point{cur.pos.R + d.R, cur.pos.C + d.C}
			if visited[next] {
				continue
			}
			if target, ok := pairs[next]; ok {
				queue = append(queue, state1{target, cur.steps + 2})
			} else if donut[next] {
				queue = append(queue, state1{next, cur.steps + 1})
			}
			visited[next] = true
		}
	}

	return -1
}

type state2 struct {
	pos   Point
	steps int
	level int
}

type visitKey struct {
	pos   Point
	level int
}

func solve2(data []string) int {
	donut, portals := parseDonut(data)
	pairs := getPortalPairs(portals)
	start := portals["AA"][0]
	end := portals["ZZ"][0]
	rows := len(data)
	cols := len(data[4])

	queue := []state2{{start, 0, 0}}
	visited := map[visitKey]bool{}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.pos == end && cur.level == 0 {
			return cur.steps
		}

		for _, d := range directions {
			next := Point{cur.pos.R + d.R, cur.pos.C + d.C}
			key := visitKey{next, cur.level}
			if visited[key] {
				continue
			}
			if target, ok := pairs[next]; ok {
				if next.R > 3 && next.R < rows-3 && next.C > 3 && next.C < cols-3 {
					queue = append(queue, state2{target, cur.steps + 2, cur.level + 1})
				} else if cur.level > 0 {
					queue = append(queue, state2{target, cur.steps + 2, cur.level - 1})
				}
			} else if donut[next] {
				queue = append(queue, state2{next, cur.steps + 1, cur.level})
			}
			visited[key] = true
		}
	}

	return -1
}

func main() {
	data := getData("inputs/20.txt")
	fmt.Printf("#1: %d\n", solve1(data))
	fmt.Printf("#2: %d\n", solve2(data))
}
