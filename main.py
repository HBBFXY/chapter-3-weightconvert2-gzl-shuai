def main():
    # 获取当前体重
    current_weight = float(input("请输入您当前的体重（kg）: "))
    
    # 月球重力系数
    moon_gravity_factor = 0.165
    
    print("\n未来10年体重变化预测:")
    print("年份\t地球体重(kg)\t月球体重(kg)")
    print("-" * 40)
    
    # 计算并输出未来10年的体重变化
    for year in range(1, 11):
        earth_weight = current_weight + year * 0.5
        moon_weight = earth_weight * moon_gravity_factor
        
        print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")

if __name__ == "__main__":
    main()
