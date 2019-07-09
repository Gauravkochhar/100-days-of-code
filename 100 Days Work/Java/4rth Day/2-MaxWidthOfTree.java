 -----------Order of the tree is :=-------------                                                             
                                                                                                             
Pre-Order                                                                                                    
5 -> 1 -> 0 -> 3 -> 7 -> 6 -> 8 ->                                                                           
In-Order                                                                                                     
0 -> 3 -> 1 -> 5 -> 6 -> 8 -> 7 ->                                                                           
Post-Order                                                                                                   
0 -> 3 -> 1 -> 6 -> 8 -> 7 -> 5 ->                                                                           
                                                                                                             
-----------Height of the tree is :=-------------                                                             
Height of tree is :-> 2                                                                                      
                                                                                                             
                                                                                                             
-------------MaxWidth of tree is :=-------------                                                             
MaxWidth of Tree is:-> 4  





class TreeNode{
    int info;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int info){
        this.info = info;
        left = right = null;
    }
    
}

class BinaryTree{
    TreeNode root;
    
    BinaryTree(TreeNode root){
        this.root = root;
    }
    
    public void visit(TreeNode node){
        System.out.print(node.info+" -> ");
    }
    
    public void preOrder(TreeNode node){
        if(node == null){
            return;
        }
        visit(node);
        preOrder(node.left);
        preOrder(node.right);
    }
    
    public void postOrder(TreeNode node){
        if(node == null){
            return;
        }
        postOrder(node.left);
        postOrder(node.right);
        visit(node);
    }
    
    public void inOrder(TreeNode node){
        if(node == null){
            return;
        }
        postOrder(node.left);
        visit(node);
        postOrder(node.right);
    }
    
    public int height(TreeNode node){
        if(node == null){
            return 0;
        }
        int height;
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        if(leftHeight >= rightHeight){
            height = leftHeight;
        }
        else{
            height = rightHeight;
        }
        return (height+1);
    }
    
    public int getWidth(TreeNode node,int level){
        if(node == null){
            return 0;
        }
        if(level == 1){
            return 1;
        }
        else if(level > 1){
            return (getWidth(node.left,level-1)+getWidth(node.right,level-1));
        }
        return 0;
    }
    
    public int getMaxWidth(TreeNode root){
        int height = height(root);
        int width = 0;
        int maxWidth = 0;
        for(int i = 0 ; i<height ; i++){
            width = getWidth(root,i+1);
            if(width>maxWidth){
                maxWidth = width;
            }
        }
        return maxWidth;
    }
   
}

public class Main
{
	public static void main(String[] args) {
	    
	    TreeNode n0 = new TreeNode(0);
	    TreeNode n1 = new TreeNode(1);
	    TreeNode n3 = new TreeNode(3);
	    TreeNode n5 = new TreeNode(5);
	    TreeNode n6 = new TreeNode(6);
	    TreeNode n7 = new TreeNode(7);
	    TreeNode n8 = new TreeNode(8);
	    n5.left = n1;
	    n5.right = n7;
	    n1.left = n0;
	    n1.right = n3;
	    n7.left = n6;
	    n7.right = n8;
	    TreeNode root = n5;
	    
	    /*
		TreeNode n1 = new TreeNode(1);
		TreeNode n2 = new TreeNode(2);
		TreeNode n5 = new TreeNode(5);
		TreeNode n6 = new TreeNode(6);
		TreeNode n7 = new TreeNode(7);
		TreeNode n9 = new TreeNode(9);
		TreeNode root = n6;
		
		n6.left = n7;
		n6.right = n9;
		n7.left = n5;
		n7.right = n2;
		n9.left = n1;
		*/
		
		BinaryTree binaryTree = new BinaryTree(root);
		System.out.println("\n -----------Order of the tree is :=-------------");
		System.out.println("\nPre-Order");
		binaryTree.preOrder(root);
		System.out.println("\nIn-Order");
		binaryTree.inOrder(root);
		System.out.println("\nPost-Order");
		binaryTree.postOrder(root);
		
		System.out.println("\n\n-----------Height of the tree is :=-------------");
		int heightOfTree = binaryTree.height(root)-1;
		System.out.println("Height of tree is :-> " + heightOfTree);
		
		System.out.println("\n\n-------------MaxWidth of tree is :=-------------");
		int maxWidth = binaryTree.getMaxWidth(root);
		System.out.println("MaxWidth of Tree is:-> " + maxWidth);
	}
}
