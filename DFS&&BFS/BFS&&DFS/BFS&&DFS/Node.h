//
//  Node.h
//  DFS&&BFS
//
//  Created by Zhou Qian on 16/10/12.
//  Copyright © 2016年 Zhou Qian. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Node : NSObject
@property (nonatomic, assign) BOOL bVisited;
@property (nonatomic, strong) NSString *name;

- (instancetype)initWithName:(NSString*)name;
- (Node*)adjacentNode:(Node*)node;
@end
