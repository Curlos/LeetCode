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
    // Use two pointers: "slow" and "fast". They will both start at the "head" node.
    let slow = head
    let fast = head

    // "slow" will increment ONE node at a time and "fast" will increment TWO nodes at a time - double the speed. Keep going until "fast" reaches the end of the linked list.
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }

    // If "fast" has reached the end of the linked list, then "slow" must be the middle node because "fast" was going TWICE as fast as "slow" so mathemtically, it lines up.
    return slow
};