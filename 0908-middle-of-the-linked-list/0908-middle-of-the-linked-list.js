/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    // Go through the whole linked list once to determine the number of nodes and keep track of this number.
    let currNode = head
    let numOfNodes = 0

    while (currNode) {
        numOfNodes++
        currNode = currNode.next
    }

    // Then, using the total number of nodes, divide that by 2 and you should have the index of the middle node in the Linked List.
    let middleIndex = Math.floor(numOfNodes / 2)

    // Using this new "middle" index, reset the current node to the head so you're at the beginning and keep go through linked list again. Again, you'll be keeping track of the current index BUT with one new condition - If the current index === middle index, then that means that this current node, must be the middle node.
    currNode = head
    let currIndex = 0

    while (currNode) {
        if (currIndex === middleIndex) {
            return currNode
        }

        currIndex++
        currNode = currNode.next
    }
};