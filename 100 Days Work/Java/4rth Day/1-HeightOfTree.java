Output:-

-----------Order of the tree is :=-------------                                                             
                                                                                                             
Pre-Order                                                                                                    
6 -> 7 -> 5 -> 2 -> 9 -> 1 ->                                                                                
In-Order                                                                                                     
5 -> 2 -> 7 -> 6 -> 1 -> 9 ->                                                                                
Post-Order                                                                                                   
5 -> 2 -> 7 -> 1 -> 9 -> 6 ->                                                                                
                                                                                                             
-----------Height of the tree is :=-------------                                                             
Height of tree is :-> 2          







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
    
   
}

public class Main
{
	public static void main(String[] args) {
	    
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
	}
}
