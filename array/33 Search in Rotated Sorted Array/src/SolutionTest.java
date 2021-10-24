import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @org.junit.jupiter.api.BeforeEach
    void setUp() {

    }
    @Test
    public void hihi()
    {   int[] nums1 = {2,4,7,9,0}; //9
        int[] nums2 = {4,5,6,7,0,1,2} ;//0
        int[] nums3 = {7,0,1,2,4,5,6};//0
        int[] nums4 = {5,1,3};//5
        int[] nums5 = {8,9,2,3,4};//9
        Solution call = new Solution();

            assertEquals(call.search(nums1, 9), 3);
            assertEquals(call.search(nums2, 3), -1);
            assertEquals(call.search(nums3, 0), 1);
            assertEquals(call.search(nums4, 5), 0);
            assertEquals(call.search(nums5, 9), 1);


    }

}