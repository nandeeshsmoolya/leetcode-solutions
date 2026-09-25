# 01. Two Sum

## Problem

Given an array of integers and a target value, return the indices of the two numbers such that they add up to the target.

## Example

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

![Two Sum Result](01-two-sum-result-png.png)

## Approach

- Use a hash map to store seen values and their indices.
- For each number, check whether the complement target - nums[i] has been seen.
- If found, return the current index and the stored index.

## Notes

This file is intended for problem explanation and solution notes.
