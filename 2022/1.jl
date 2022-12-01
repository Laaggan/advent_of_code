function solve()
    f = open("1_real_data.txt")
    i = 0
    cum_sum = 0
    max_value = 0
    max_index = -1
    for line in eachline(f)
        if (line == "")
            #println(cum_sum)
            if cum_sum > max_value
                max_index = i
                max_value = cum_sum
            end
            i += 1
            cum_sum = 0
        else
            cum_sum += parse(Int64, line)
        end
    end
    print(max_value)
end

solve()