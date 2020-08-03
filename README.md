<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="GetPrefixSetIOSXR_0"></a>Get-PrefixSet-IOS-XR</h1>
<p class="has-line-data" data-line-start="3" data-line-end="4"><a href="https://developer.cisco.com/codeexchange/github/repo/AnasProgrammer2/Get-PrefixSet-IOS-XR"><img src="https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg" alt="published"></a></p>
<p class="has-line-data" data-line-start="5" data-line-end="6">PrefixSet-IOS-XR is a automation Tool that help you to get prefix-set from Router Cisco IOS XR , as Datatype [JSON | YAML]</p>
<ul>
<li class="has-line-data" data-line-start="7" data-line-end="8">it’s too fast</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">support ipv4 &amp; ipv6 prefix-set</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">help your to control a prefix-set that’s used in BGP adverting with ISP</li>
</ul>
<h3 class="code-line" data-line-start=16 data-line-end=17 ><a id="Installation_16"></a>Installation</h3>
<p class="has-line-data" data-line-start="19" data-line-end="20">Install the dependencies and devDependencies and start the server.</p>
<pre><code class="has-line-data" data-line-start="22" data-line-end="26" class="language-sh"><span class="hljs-comment">#git clone https://github.com/AnasProgrammer2/Get-PrefixSet-IOS-XR.git</span>
<span class="hljs-comment">#cd Get-PrefixSet-IOS-XR/</span>
<span class="hljs-comment">#pip3 install -r requirements.txt</span>
</code></pre>
<h4 class="code-line" data-line-start=28 data-line-end=29 ><a id="syntax_28"></a>syntax</h4>
<p class="has-line-data" data-line-start="29" data-line-end="30">For production release:</p>
<pre><code class="has-line-data" data-line-start="31" data-line-end="33" class="language-sh"> <span class="hljs-comment">#Python3 Get_PrefixSet_XR.py  [Hostname]  [UserName]  [Password]  [TYPE(YAML|JSON)]</span>
</code></pre>
<p class="has-line-data" data-line-start="33" data-line-end="37">Hostname : Router  IP address<br>
UserName : Username Router Loign<br>
Password : Password Router Loign<br>
TYPE : Type Data OutPut JSON OR YAML</p>
<h3 class="code-line" data-line-start=40 data-line-end=41 ><a id="Exmaple_40"></a>Exmaple</h3>
<pre><code class="has-line-data" data-line-start="43" data-line-end="45" class="language-sh"><span class="hljs-comment">#Python3 Get_PrefixSet_XR.py  10.10.20.1  cisco  cisco123  JSON</span>
</code></pre>
<p class="has-line-data" data-line-start="45" data-line-end="47">the output result<br>
<img src="https://user-images.githubusercontent.com/15816300/89223032-bd15cd00-d5de-11ea-9619-fefcacdefa80.png" alt="Prefix_set_get"></p>
