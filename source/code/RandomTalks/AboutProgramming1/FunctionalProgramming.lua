local function get_accumulator(start)
    start = start or 0
    return function()
        start = start + 1
        return start
    end
end

local acc = get_accumulator()
for i = 1, 10, 2 do
    print(acc())
end