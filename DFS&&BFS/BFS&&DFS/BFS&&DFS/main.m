//
//  main.m
//  BFS&&DFS
//
//  Created by Zhou Qian on 16/10/12.
//  Copyright © 2016年 Zhou Qian. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Node.h"
#import "Stack.h"

Node* getUnvisitedAdjacentNode(Node *n, NSArray* graph) {
    Node *result = nil;
    for (NSArray *list in graph) {
        Node *firstNode = [list firstObject];
        if ([n.name isEqualToString:firstNode.name]) {
            for (Node *node in list) {
                if (node.bVisited == NO) {
                    result = node;
                    break;
                }
            }
            break;//该节点的所有相邻节点都访问过了
        }
    }
    return result;
}

void dfs(Node *root, NSArray *graph) {
    NSLog(@"begin dfs algorithm");
    Stack *s = [[Stack alloc] init];
    root.bVisited = YES;
    NSLog(@"%@", root);
    [s push:root];
    
    while ([s isEmpty] == NO) {//当s为空时，说明所有节点及其邻接点都遍历过
        Node *n = (Node*)[s peek];
        Node *child = getUnvisitedAdjacentNode(n, graph);
        if (child) {
            child.bVisited = YES;
            NSLog(@"%@", child);
            [s push:child];
        }
        else {
            [s pop];
        }
    }
}

void bfs(Node *root, NSArray *graph) {
    NSLog(@"begin bfs algorithm");
    NSMutableArray *q = [[NSMutableArray alloc] init];
    root.bVisited = YES;
    NSLog(@"%@", root);
    [q addObject:root];
    
    while (q.count != 0) {
        Node *node = [q firstObject];
        Node *child = getUnvisitedAdjacentNode(node, graph);
        if (child) {
            child.bVisited = YES;
            NSLog(@"%@", child);
            [q addObject:child];
        }
        else {
            [q removeObjectAtIndex:0];
        }
    }
    
}

void cleanTestData(NSArray *graph) {
    for (NSArray *arr in graph) {
        for (Node *node in arr) {
            node.bVisited = NO;
        }
    }
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        Node *a = [[Node alloc] initWithName:@"A"];
        Node *b = [[Node alloc] initWithName:@"B"];
        Node *c = [[Node alloc] initWithName:@"C"];
        Node *d = [[Node alloc] initWithName:@"D"];
        Node *e = [[Node alloc] initWithName:@"E"];
        Node *f = [[Node alloc] initWithName:@"F"];
        
        NSArray *aList = @[a, b, c, d];
        NSArray *bList = @[b, a, e, f];
        NSArray *cList = @[c, a, f];
        NSArray *dList = @[d, a];
        NSArray *eList = @[e, b];
        NSArray *fList = @[f, b, c];
        
        NSArray *graph = @[aList, bList, cList, dList, eList, fList];
        cleanTestData(graph);
        dfs(a, graph);
        cleanTestData(graph);
        bfs(a, graph);
    }
    return 0;
}
