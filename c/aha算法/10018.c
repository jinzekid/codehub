#include <stdio.h>

int a[12];
int DEFAULTMONEY = 300;

int main() {

    int i;
    int flag = 0;
    int noMoneyMonth = 0;
    int leftMoney = 0;
    int moneyGiveToMama = 0;
    int totalGiveBackMoney = 0;
    int n;
    // 输入12行数据，每个月的预算
    for (i = 0; i < 12; i++) {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < 12; i++) {
        leftMoney += (DEFAULTMONEY - a[i]); //第i个月的剩余钱: 上月余钱+妈妈给的300-预算

        // 对剩余钱进行判断，如果不够，就需要跳出循环显示月份
        if (leftMoney < 0) {
            flag = 1;
            noMoneyMonth = i+1;
        }
        if (flag == 1) {
            break;
        }
        
        // 计算需要给妈妈的钱
        n = leftMoney/100;
        if (n > 0) {
            moneyGiveToMama += n*100; // 转存给妈妈
        }

        leftMoney = leftMoney - n*100; // 第i个月剩余钱
    }


    if (flag == 1) {
        printf("-%d\n", noMoneyMonth);
    }
    else {
        totalGiveBackMoney = moneyGiveToMama + moneyGiveToMama * 0.2 + leftMoney; // 总共的钱：存的钱+妈妈加上的20%的钱+剩余的钱
        printf("%d\n", totalGiveBackMoney);
    }


    return 0;
}
