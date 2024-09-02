/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var checkTree = function (root) {
    const leftValue = root?.left?.val || 0
    const rightValue = root?.right?.val || 0
    const sumOfTheChildren = leftValue + rightValue

    return root.val === sumOfTheChildren
};