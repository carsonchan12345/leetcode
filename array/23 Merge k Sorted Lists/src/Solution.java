/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length==0)
            return null;
        PriorityQueue<Integer> tmp = new PriorityQueue<Integer>();
        ListNode tmp2;
        ListNode res = new ListNode();
        Integer[] tmp3;
        for (int i=0; i<lists.length; i++)
        {
            tmp2=lists[i];
            while(tmp2!=null)
            {
                tmp.add(tmp2.val);
                tmp2=tmp2.next;
            }
        }
        tmp2=res;
        if (tmp.peek()==null)
        {
            return null;
        }
        while(tmp.peek()!=null)
        {
            tmp2.val=tmp.poll();
            if (tmp.peek()!=null)
            {            tmp2.next=new ListNode();
                tmp2=tmp2.next;}
        }
        return res;

    }
}