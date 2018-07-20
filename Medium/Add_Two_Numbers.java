/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result;
        // Initialize the result;
        int sum = (l1.val + l2.val)%10;
        int c = (l1.val + l2.val)/10;
        result = new ListNode(sum);
        
        l1 = l1.next;
        l2 = l2.next;
        if (c!=0){
            result.next = new ListNode(c);
        }
        // Addition
        ListNode s = result;
        
        while (l1 != null){
            s.next = new ListNode(c);
            s = s.next;
            if (l2 != null){
                sum = (l1.val + l2.val + s.val)%10;
                c = (l1.val + l2.val + s.val)/10;
                s.val = sum;
                l2 = l2.next;
            }
            else{
                sum = (l1.val + s.val)%10;
                c = (l1.val+s.val)/10;
                s.val = sum;
            }
            l1 = l1.next;
        }

      while (l2 !=null){
          s.next = new ListNode(c);
          s = s.next;
          sum = (l2.val + s.val )%10;
          c = (s.val + l2.val)/10;
          s.val = sum;
          l2 = l2.next;
      }
        if (c != 0){
            s.next = new ListNode(c);
            s = s.next;
          }
    return result;
    }
}
