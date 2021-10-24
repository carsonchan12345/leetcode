/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {

    HashSet<ListNode> cars = new HashSet<ListNode>();

    public boolean hasCycle(ListNode head) {
        if (head==null)
            return false;

        ListNode tmp=head;
        while(tmp.next!=null)
        {  cars.add(tmp);
            if (cars.contains(tmp.next))
                return true;
            tmp = tmp.next;
        }
        return false;

    }
}

or

