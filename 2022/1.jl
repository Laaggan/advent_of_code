function solve1()
    f = open("data/1_real_data.txt")
    i = 0
    cum_sum = 0
    max_value = 0
    max_index = -1
    for line in eachline(f)
        if (line == "")
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

function solve2()
    f = open("data/1_real_data.txt")
    
    data = read(f, String)
    data = replace(data, "\r" => "")
    data = collect(eachsplit(data, "\n"))
    println(data)
    data = split_array(data, "")
    f = x -> parse(Int32, x)
    data = map(x -> map(f, x), data)
    println(data)
    
    println(sort(map(sum, data), rev=true))
    println(sum(sort(map(sum, data), rev=true)[1:3]))
end

function split_array(array, split_value)
    final_result = []
    intermediate_result = []
    for (index, element) in enumerate(array)
        if (element == split_value)
            push!(final_result, intermediate_result)
            intermediate_result = []
            continue
        elseif (index == length(array))
            push!(final_result, intermediate_result)
        end
        push!(intermediate_result, element)
    end
    return final_result
end

#solve1()
solve2()