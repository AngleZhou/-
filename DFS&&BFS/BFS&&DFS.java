public class MainActivity extends AppCompatActivity {    
    private List<List<Node>> graphList;    
    public class Node {        
        char nodeName;        
        boolean isVisited;        
        public Node(char name) {
            nodeName = name;
        }        
        public boolean isVisited() {            
            return isVisited;
        }        
        public void setVisited(boolean visited) {
            isVisited = visited;
        }        
        public char getNodeName() {            
            return nodeName;
        }        
        public void printNode(){
            Log.d("DailyPractice", "printing graph node with name: " + nodeName);
        }
    }    
    @Override
    protected void onCreate(Bundle savedInstanceState) {        
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);        //prepare test graph
        Node a = new Node('A');
        Node b = new Node('B');
        Node c = new Node('C');
        Node d = new Node('D');
        Node e = new Node('E');
        Node f = new Node('F');        //use adjacency list to represent graph
        List<Node> aList = Arrays.asList(a, b, c, d);
        List<Node> bList = Arrays.asList(b, a, e, f);
        List<Node> cList = Arrays.asList(c, a, f);
        List<Node> dList = Arrays.asList(d, a);
        List<Node> eList = Arrays.asList(e, b);
        List<Node> fList = Arrays.asList(f, b, c);

        graphList = Arrays.asList(aList, bList, cList, dList, eList, fList);        //start dfs : A B C D E F
        cleanTestData();
        dfs(a);        //start bfs : A B C D E F
        cleanTestData();
        bfs(a);
    }    

    public void dfs(Node root)
    {
        Log.d("DailyPractice", "begin dfs algorithm");
        Stack s = new Stack();
        root.setVisited(true);
        root.printNode();
        s.push(root);        
        while (s.isEmpty() == false)
        {
            Node n = (Node)s.peek();
            Node child = getUnvisitedAdjacentNode(n);            
            if (child != null){
                child.setVisited(true);
                child.printNode();
                s.push(child);
            }            
            else
            {
                s.pop();
            }
        }
    }    
    public void bfs(Node root)
    {
        Log.d("DailyPractice", "begin bfs algorithm");
        Queue<Node> q = new LinkedList<>();
        root.setVisited(true);
        root.printNode();
        q.add(root);        
        while (q.isEmpty() == false)
        {
            Node node = q.peek();
            Node child = getUnvisitedAdjacentNode(node);            
            if (child != null)
            {
                child.setVisited(true);
                child.printNode();
                q.add(child);
            }            
            else
            {
                q.remove();
            }
        }

    }    

    public Node getUnvisitedAdjacentNode(Node n){
        Node result = null;        
        for (List<Node> list : graphList) {
            Node firstNode = list.get(0);            
            if (firstNode.getNodeName() == n.getNodeName())
            {                
                for (Node node : list)
                {                    
                    if (node.isVisited() == false)
                    {
                        result = node;                        
                        break;
                    }
                }                
                break;
            }
        }        
        return result;
    }    

    public void cleanTestData()
    {        
        for (List<Node> list : graphList)
        {            
            for (Node node : list)
            {
                node.setVisited(false);
            }
        }
    }
}