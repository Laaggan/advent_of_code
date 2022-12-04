function read_file()
    f = open("data/3_real_data.txt")
    data = read(f, String)
    data = collect(eachsplit(data, "\r\n"))
    return data
end

function solve_part_1()
    data = read_file()
    final_value = 0

    for rucksack in data
        types = Dict{Char, Int64}()
        n = length(rucksack)
        rucksack_size = convert(Int64, n/2)

        rucksack_1 = rucksack[1:rucksack_size]
        rucksack_2 = rucksack[(rucksack_size + 1):end]

        for c in rucksack_1
            if (!haskey(types, c))
                types[c] = 1
            else
                types[c] = types[c] + 1
            end
        end

        for c in rucksack_2
            if (haskey(types, c))
                points = convert_char_to_points(c)
                final_value += points
                break
            end
        end
    end
    println(final_value)
end

function convert_char_to_points(c::Char)::Int32
    v = Int(c)
    if (v > 96 && v < 123)
        return v - 96
    elseif (v > 64 && v < 91)
        return v - 64 + 26
    end
end

solve_part_1()