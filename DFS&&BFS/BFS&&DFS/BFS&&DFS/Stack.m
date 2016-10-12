//
//  Stack.m
//  BFS&&DFS
//
//  Created by Zhou Qian on 16/10/12.
//  Copyright © 2016年 Zhou Qian. All rights reserved.
//

#import "Stack.h"

@interface Stack ()
@property (nonatomic, strong) NSMutableArray *arr;
@end
@implementation Stack

- (instancetype)init {
    if (self = [super init]) {
        _arr = [[NSMutableArray alloc] init];
    }
    return self;
}

- (void)push:(id)obj {
    [self.arr addObject:obj];
}

- (id)pop {
    id obj = [self.arr lastObject];
    [self.arr removeLastObject];
    return obj;
}

- (BOOL)isEmpty {
    return self.arr.count == 0;
}

- (id)peek {
    return self.arr.lastObject;
}
@end
