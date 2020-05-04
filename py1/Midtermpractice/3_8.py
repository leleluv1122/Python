name = input("사원이름을 입력하세요: ")
hours = eval(input("주당 근무시간을 입력하세요: "))
h_money = eval(input("시간당 급여를 입력하세요: "))
won_per = eval(input("원천징수세율을 입력하세요: "))
gi_per = eval(input("지방세율을 입력하세요: "))

w = won_per*hours*h_money
g = gi_per*hours*h_money
f = hours*h_money - w - g
print("사원 이름:" + name)
print("주당 근무시간:", hours)
print("임금:",h_money)
print("총 급여:",hours*h_money)
print("공제:")
print("  원천징수세 (",format(won_per*100,".1f"),"%): ", format(w,".0f"))
print("  주민세 (",format(gi_per*100,".1f"),"%): ", format(g, ".0f"))
print("  총 공제: ", format(g+w,".0f"))
print("공제 후 급여: ", format(f, ".0f"))