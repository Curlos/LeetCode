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
    let numOfNodes = 1
    let currNode = head

    // We need to go to the end of the linked list. We'll know we're at the end of the linked list once the ".next" node is null or undefined.
    // 1, 2, 3, 4, 5
    while (currNode.next) {
        numOfNodes += 1
        currNode = currNode.next
    }

    const middleIndex = Math.floor(numOfNodes / 2)
    let currIndex = 0

    currNode = head

    while (currIndex < middleIndex) {
        currIndex += 1

        currNode = currNode.next
    }


    return currNode
};