use_osc "localhost", 10000

live_loop :ban do
  use_real_time
  n, v = sync "/midi:circuitpython_audio_1:1/note_on"
  osc "/interactive/box2", 1
  if v!=0
    synth :pnoise, note: n
    osc "/interactive/box1", rrand(0, 3)
    osc "/interactive/box2", 0
    sleep 0.25
  end
  osc "/interactive/box2", 1
end

define :pp do |n,t|
  play n, amp: 0.5, attack: 0, attack_level: 1, decay: 0, sustain_level: 1, sustain: t, release: 0
  sleep t
end

time = [0.75,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1]
m1 = [:C4,:G4,:C5,:C5,:C5,:C5,:C5,:G4,:A4,:C5,:C5,:A4,:G4]
m2 = [:C4,:G4,:C5,:C5,:C5,:C5,:C5,:G4,:A4,:G4,:E4,:D4,:C4]
live_loop :trumpet do
  use_bpm 137
  use_synth :bass_foundation
  for i in 0...time.length
    pp m1[i], time[i]
  end
  sleep 1
  for i in 0...time.length
    pp m2[i], time[i]
  end
  sleep 1
end