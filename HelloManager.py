class HelloManager:
    def __init__(self, date, money, category, note):
        self.date = date
        self.money = money
        self.category = category
        self.note = note

bill = []

while True:
    print("=================================")
    print("欢迎使用个人账单管理系统")
    print("=================================")
    print("请选择操作：")
    print("1. 记录收入")
    print("3. 查看所有账单")
    print("4. 查询账单")
    print("2. 记录支出")
    print("5. 退出系统")

    a = input("请输入选项序号：")

    if a == "1":
        date = input("日期（Year-Month-Date）：")
        money = float(input("金额："))
        if money <= 0:
            print("收入金额必须为正数。")
            continue
        category = input("类别（如工资、奖金等）：")
        note = input("备注：")
        bill.append(HelloManager(date, money, category, note))
        print("收入已成功记录！")
    elif a == "2":
        date = input("日期（Year-Month-Date）：")
        money = float(input("金额："))
        if money <= 0:
            print("支出金额必须为正数。")
            continue
        category = input("类别（如餐饮、交通、购物等）：")
        note = input("备注：")
        bill.append(HelloManager(date, -money, category, note))
        print("支出已成功记录！")
    elif a == "3":
        print("收入账单信息如下：")
        for bill1 in bill:
            if bill1.amount > 0:
                print(f"{bill1.date}，收入，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
        print("支出账单信息如下：")
        for bill1 in bill:
            if bill1.amount < 0:
                print(f"{bill1.date}，支出，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
    elif a == "4":
        print("请选择查询的方式：")
        print("1. 按指定日期查询")
        print("2. 按日期范围查询")
        print("3. 按类别查询")
        b = input("请输入查询方式序号：")
        if b == "1":
            b_date = input("请输入要查询的日期（YYYY-MM-DD）：")
            print("收入账单信息如下：")
            for bill1 in bill:
                if bill1.amount > 0 and bill1.date == b_date:
                    print(f"{bill1.date}，收入，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
            print("支出账单信息如下：")
            for bill1 in bill:
                if bill1.amount < 0 and bill1.date == b_date:
                    print(f"{bill1.date}，支出，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
        elif b == "2":
            s_date = input("请输入开始日期（YYYY-MM-DD）：")
            e_date = input("请输入结束日期（YYYY-MM-DD）：")
            print("收入账单信息如下：")
            for bill1 in bill:
                if bill1.amount > 0 and s_date <= bill1.date <= e_date:
                    print(f"{bill1.date}，收入，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
            print("支出账单信息如下：")
            for bill1 in bill:
                if bill1.amount < 0 and s_date <= bill1.date <= e_date:
                    print(f"{bill1.date}，支出，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
        elif b == "3":
            b_category = input("请输入要查询的类别：")
            print("收入账单信息如下：")
            for bill1 in bill:
                if bill1.amount > 0 and bill1.category == b_category:
                    print(f"{bill1.date}，收入，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
            print("支出账单信息如下：")
            for bill1 in bill:
                if bill1.amount < 0 and bill1.category == b_category:
                    print(f"{bill1.date}，支出，金额：{bill1.amount}，类别：{bill1.category}，备注：{bill1.note}")
        else:
            print("无效的查询方式序号，请重新输入。")
    elif a == "5":
        print("再见！")
        break
    else:
        print("无效选项，请重新输入。")