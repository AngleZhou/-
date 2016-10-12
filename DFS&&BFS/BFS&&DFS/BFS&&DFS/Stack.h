//
//  Stack.h
//  BFS&&DFS
//
//  Created by Zhou Qian on 16/10/12.
//  Copyright © 2016年 Zhou Qian. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Stack : NSObject

- (void)push:(id)obj;
- (id)pop;

- (BOOL)isEmpty;
- (id)peek;
@end
