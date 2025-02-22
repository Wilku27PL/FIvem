-- This file contains the main logic for the aim assist feature.
local aimAssistEnabled = true
local aimSensitivity = 0.5

-- Function to obfuscate the script
local function obfuscateScript()
    -- Placeholder for obfuscation logic
    -- This could include renaming variables, encoding strings, etc.
end

-- Function to check for anti-cheat detection
local function checkForAntiCheat()
    -- Placeholder for anti-cheat detection logic
    -- This could include checking for known anti-cheat processes, files, etc.
    return false
end

function onPlayerInput()
    if aimAssistEnabled then
        local playerPed = PlayerPedId()
        local targetPed = getClosestEnemy()

        if targetPed then
            local targetCoords = GetEntityCoords(targetPed)
            local playerCoords = GetEntityCoords(playerPed)
            local aimDirection = vector3(targetCoords.x - playerCoords.x, targetCoords.y - playerCoords.y, targetCoords.z - playerCoords.z)

            local aimAdjustment = aimDirection * aimSensitivity
            SetEntityRotation(playerPed, aimAdjustment.x, aimAdjustment.y, aimAdjustment.z, 2, true)
        end
    end
end

function getClosestEnemy()
    local closestEnemy = nil
    local closestDistance = 999.0

    for _, player in ipairs(GetActivePlayers()) do
        local playerPed = GetPlayerPed(player)
        if playerPed ~= PlayerPedId() and IsEntityVisible(playerPed) then
            local distance = Vdist(GetEntityCoords(PlayerPedId()), GetEntityCoords(playerPed))
            if distance < closestDistance then
                closestDistance = distance
                closestEnemy = playerPed
            end
        end
    end

    return closestEnemy
end

if Citizen then
    Citizen.CreateThread(function()
        obfuscateScript()
        while true do
            Citizen.Wait(0)
            if checkForAntiCheat() then
                print("Anti-cheat detected. Disabling aim assist.")
                aimAssistEnabled = false
            end
            if IsControlJustPressed(1, 213) then -- 213 is the control ID for the "Home" key
                aimAssistEnabled = not aimAssistEnabled
                print("Aim Assist " .. (aimAssistEnabled and "Enabled" or "Disabled"))
            end
            if aimAssistEnabled then
                onPlayerInput()
            end
        end
    end)
else
    print("Citizen is not available in this environment.")
end
