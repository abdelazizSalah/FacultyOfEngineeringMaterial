% clearing the previous
clc;
close all;
clear all;

% reading the audio
[mySignal, mySignalFreq] = audioread('myRecord.m4a');


%ploting the time domain

% Signal Time step should be with length(mySignal)/mySignalFreq per step
t = linspace(0, length(mySignal)/mySignalFreq , length(mySignal)); 
f = -mySignalFreq/2 : mySignalFreq/length(t) : mySignalFreq/2 - mySignalFreq/length(t);
figure(1);
plot(t, mySignal);
title ('myAudio in time domain');
xlabel('time');
ylabel('amplitude');


%plotting frequency domain
messageFreq = fftshift(fft(mySignal));
figure(2);
plot(f, abs(messageFreq));
title ('myAudio in frequancy domain');
ylabel('amplitude');
xlabel('freq');

% ploting the phase
figure(3);
plot(f, unwrap(angle(messageFreq)));
title ('myAudio in frequancy domain');
ylabel('phase');
xlabel('freq');



% Modulation phase
CarrierTime = cos(2*pi*9000*t);
CarrierFreq = abs(fftshift(fft(CarrierTime)))/mySignalFreq;

% Modulation idx.
ModulationIdx = 0.8;
Ac = abs(min(mySignal))/ModulationIdx;
SignalTime = (mySignal + Ac).*CarrierTime';

% plotting the signal after the modualtion in time
figure(4);
plot(t,SignalTime);
title ('After Modulation');
xlabel('time');
ylabel('amplitude');


% plotting the signal after the modualtion in frequancy
SignalFreq = fftshift(fft(SignalTime));
figure(5);
plot(f, abs(SignalFreq));
title ('modulation freq domain');
xlabel('freq');
ylabel('amplitude');

% plotting the signal after the modualtion in frequancy in phase
figure(6);
plot(f, unwrap(angle(SignalFreq)));
title ('modulation freq domain');
xlabel('freq');
ylabel('phase');

% Demodulation phase. 
RecivedSignal = SignalTime.*CarrierTime';
RecivedSignal_after_lowPassFilter = lowpass(RecivedSignal,9000, mySignalFreq, 'SignalTimeeepness', 0.95);

RecivedSignal_after_lowPassFilter = RecivedSignal_after_lowPassFilter - 0.5*Ac;

% playing the message to ensure that it is the same and working.
sound (RecivedSignal_after_lowPassFilter, mySignalFreq);

%plotting the signal in the time domain
figure(7);
plot(t,RecivedSignal_after_lowPassFilter);
title ('After deModulation');
xlabel('time');
ylabel('amplitude');


%plotting the signal in the frequancy domain in amplitude.
RecivedSignal_after_lowPassFilter_freq = fftshift(fft(RecivedSignal_after_lowPassFilter));
figure(8);
plot(f, abs(RecivedSignal_after_lowPassFilter_freq));
title ('demodulation freq domain');
xlabel('freq');
ylabel('amplitude');


%plotting the signal in the frequancy domain in phase.
figure(9);
plot(f, unwrap(angle(RecivedSignal_after_lowPassFilter_freq)));
title ('demodulation freq domain');
xlabel('freq');
ylabel('phase');