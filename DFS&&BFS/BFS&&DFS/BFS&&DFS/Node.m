//
//  Node.m
//  DFS&&BFS
//
//  Created by Zhou Qian on 16/10/12.
//  Copyright © 2016年 Zhou Qian. All rights reserved.
//

#import "Node.h"

@implementation Node

- (instancetype)initWithName:(NSString*)name {
    if (self = [super init]) {
        self.name = name;
    }
    return self;
}
- (NSString*)description {
    return self.name;
}
@end
