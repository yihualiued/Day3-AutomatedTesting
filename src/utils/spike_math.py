


# %%  Count Spikes Function
# 
# 1. Write Automated Tests that answer the following questions:
#    - is this function correct when 3 spikes are given?
#    - is this function correct when 0 spikes are given?
#    - is this function correct when the spikes are given as tuple (round parentheses), instead of a list?
# 
# 2. Refactor the function: Make it nicer to read, while stil passing all the tests.
#    - Idea: len()


def count_spikes(spikes):
    total = 0
    for spike in spikes:
        total += 1
    return total

count_spikes([1, 5, 6, 8])



# %%  Compute Inter-Spike-Interval Function
# 
# 1. Write Automated Tests that answer the following questions:
#    - is this function correct when four spikes are given?
#    - is this function correct when 1 spike is given?
#    - is this function correct when 0 spikes are given?
#    - is this function correct when spikes with negative numbers are given?
# 
# 2. Refactor the function: Make it nicer to read, while stil passing the tests.
#    - idea: numpy.diff().tolist()
#
# (For Second Breakout Session): Improve the function: Write a test that shows the function fails, then improve the function to pass the test.
#   - This function fails when the spikes are not given in order.


def compute_isi(spikes):
    isis = []
    for spike1, spike2 in zip(spikes[:-1], spikes[1:]):
        isi = spike2 - spike1
        isis.append(isi)
    return isis


compute_isi([1, 3, 6])

# %% Compute Mean Firing Rate
# 
# 1. Write Automated Tests that answer the following questions:
#    - is this function correct when the spikes are all at a regular interval?
#    - is this function correct when the total time is given?
# 
# 2. Refactor the function: Make it nicer to read, while stil passing the tests.
#    - idea: min(), max()
#    - idea: count_spikes()
#
# (For Second Breakout Session): Improve the function: Write a test that shows the function fails, then improve the function to pass the test.
#   - This function fails when the spikes all happen at the same time.
#      - idea: float("inf")
#   - This function is incorrect when the total_secs is less than the spiking period.
#      - idea: raise ValueError("total_secs not high enough for this spike train.")


def mean_firing_rate(spikes, total_secs=None):
    if total_secs is None:
        min_secs = spikes[0]
        max_secs = spikes[1]
        for spike in spikes:
            if spike > max_secs:
                max_secs = spike
            if spike < min_secs:
                min_secs = spike
        total_secs = max_secs - min_secs
        
    total_spikes = 0
    for spike in spikes:
        total_spikes += 1
    return total_spikes / total_secs


mean_firing_rate(spikes=[1, 4], total_secs=2)



# %%  Making a nice title
# 
# 1. Write Automated Tests that answer the following questions:
#    - Does this function work when there is an underscore in the name?
#    - Does this function work when no units are given?
# 
# 2. Refactor the function: Make it nicer to read, while stil passing the tests.
#    - idea: f"{var1}: {var2}"


def variable_title(ax, variable_name, units = None):
    title = ""
    title += variable_name.replace('_', ' ').title()
    if units is not None:
        title += ' '
        title += '('
        title += units.replace('_', ' ').title()
        title += ')'

    ax.set_title(title)



import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 2, 4])
ax = plt.gca()
variable_title(ax, 'firing rate', 'hz')
text = ax.title.get_text()
text
