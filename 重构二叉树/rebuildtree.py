#-*-coding:utf-8-*-


## 前序遍历结果 1,2,4,7,3,5,6,8
## 中序遍历结果 4,7,2,1,5,3,8,6

#基本思路
#递归分组
'''
根节点1 
左子树 4,7,2
右子树 5,3,8,6
'''

'''
根节点2 
左子树 4,7,2
右子树 空
'''

'''
根节点4
左子树 空
右子树 7
'''

'''
根节点3
左子树 5
右子树  6 8
'''

'''
根节点 6
左子树 8
右子树 空
'''

class BinaryTree:
    """树节点"""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Rebuilder:
    def rebuild_binary_tree(self, pre, tin):
        """根据前序遍历和中序遍历来重建一颗二叉树，
        必须要求前序遍历和中序遍历当中字符不重复，否则无法做分割递归定位
        Args:
          pre: 前序遍历  
          mid: 中序遍历  
        Returns：
          head: 一个BinaryTree类型的根节点
        """
        return self.rebuild_tree(pre, 0, len(pre)-1, mid, 0, len(mid)-1)
 
    def rebuild_tree(self, pre, pre_start, pre_end, mid, mid_start, mid_end):
        """递归的进行树的重建"""
        if pre_start > pre_end or mid_start > mid_end:
            return None
 
        head = BinaryTree(pre[pre_start])
        mid_mid = mid.index(pre[pre_start])
        left_length = mid_mid - mid_start
 
        head.left = self.rebuild_tree(pre, pre_start+1, pre_start+left_length, 
                                      mid, mid_start, mid_mid-1)
        head.right = self.rebuild_tree(pre,pre_start+left_length+1, pre_end, 
                                       mid, mid_mid+1, mid_end)
                                       
        return head
 
def after_order_print(head):
    """
    以后序遍历的方式打印一颗二叉树
    """
    if head is None:
        return
    after_order_print(head.left)
    after_order_print(head.right)
    print(head.val,end='')
if __name__ == '__main__':
    pre = '12473568'
    mid = '47215386'
    s = Rebuilder()
    head = s.rebuild_binary_tree(pre, mid)
    after_order_print(head)  # result: DGEBHFCA



