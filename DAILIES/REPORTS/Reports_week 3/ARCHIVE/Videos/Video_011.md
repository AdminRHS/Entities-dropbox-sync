# Wan 2.2 Open Source Video Generation - First Look

### 1. Metadata Section
- **Video Title**: Wan 2.2 Open Source Video Generation - First Look
- **Channel/Creator**: Benji AI
- **Video URL**: [Not provided]
- **Duration**: 31:12
- **Publication Date**: [Not available]

### 2. Description Section
- **Description**: This video provides a first look and initial impressions of the Wan 2.2 open-source AI video generation model. It covers the new features, different model versions, and how to run them using ComfyUI. The creator explores the model's capabilities, including lighting, camera angle control, text-to-video, and image-to-video generation.
- **Key Topics**:
  - Introduction to Wan 2.2 open-source release.
  - New features: lighting control, time switch, camera angles, saturation, composition.
  - Model types: Text-to-Video (T2V), Image-to-Video (I2V), and a hybrid model.
  - Mixture of Experts (MoE) architecture.
  - Hardware requirements (VRAM consumption).
  - How to run Wan 2.2 in ComfyUI.
  - Workflow examples for different model sizes (5B and 14B).
  - Comparison of video quality between different models and settings.
- **Links Referenced**:
  - [GitHub Repo for Wan 2.2]
  - [Hugging Face page for Wan AI]
  - [ComfyUI Blog post on Wan 2.2 integration]

### 3. Word-for-Word Transcription

[00:00] Hello everyone. So, today is finally here. The one 2.2 open source AI video model has been released on hugging face and in model scope. Now, as you can see, there are many new features within this model. You can change different lighting backgrounds, adjust timing like day and night, and even camera angles, all of which are trained by default into the one 2.2 models. You don't need any additional Lora for that.

[00:27] These camera angles and special effects actions, especially this one, are pretty cool. The high saturations and low saturations of video displays, as well as more compositions of objects in the videos are now included in the one 2.2 AI models. Now, today we're going to check it out more, kind of like first impressions after using it for a night. And I'm going to stay open-minded and not be too opinionated. You guys can judge whether this is suitable for you or not to run your AI video generation.

[00:57] So, first, we're going to check out the GitHub repo of one 2.2. This is a separate GitHub project and it's been updated about 5 hours ago for releasing this GitHub project. This AI model is under the Apache 2.0 license, which obviously makes it a real open-source model that you can use privately or commercially. One thing that's really cool about this model, when I tried it out and downloaded it on day zero, is that it's already integrated into the Comfy UI and there's also diffuser integration, which lets us load transformer architecture models within diffusers. You can run it with Python code and generate videos programmatically, but in this video, I'm going more for the user-friendly way, which is using Comfy UI. We're running the node-based app to run the AI models.

[01:46] Now, scroll down a little bit here and we've got a chart listing the models released today for 1 2.2. You'll see that this AI model is kind of funny. We have three types of models listed here, which obviously makes sense. We've got text-to-video and image-to-video. But the last part, which you see in the third row, is a mixture of text-to-video and image-to-video combined together. And this supports 720p resolution, which is really cool. This is a highly compressed AI model using the new VAE from WAN 2.2.

[02:18] Now this will show up later and you'll understand what I mean when I talk about using the new VAE of WAN 2.2. Going back to the first two rows, these two giants are MOE models. MOE stands for Mixture of Experts, a new method of training AI models that's trending this year. A lot of language models are also using the MOE method to train, activating different expert data sets during the execution process. This means it's not going to load every single data set parameter when you run the AI models, which makes it a little more cost-effective or cost-efficient, I should say, for running large models like this.

[02:56] Now coming back here, we see that it's set for 24 FPS by default, supporting a model with 5 billion parameters. The hybrid support model is also using 24 frames per second and we're going to check out how they run on hugging face right now. So, on hugging face, when you go to the one AI hugging face page, you'll see that a list of new AI models for one 2.2 has already been uploaded. We've got the image to video A 14B, which is the MOE method trained model they call A 14B, and then the text-to-video, which is T2V A 14B again.

[03:35] One thing you'll notice is the TI 2V 5B. This is the hybrid model I was just talking about, combining text-to-video and image-to-video together with a 5 billion parameter model. Now, in this video, I'm going to show more about this model rather than those two giant models because, well, those two giant models are still nice to run, but they consume a lot of VRAM. And I mean a lot of VRAM.

[04:00] So, for most of you guys using local AI, the best option is probably Comfy UI to run this. The most convenient way to run when 2.2 on day zero is already supported in Comfy UI, which you can see explained in their blog post on the official Comfy UI website. There's an explanation of the template for running one 2.2 in the latest update of Comfy UI itself. First, you need to update your Comfy UI. If you have previous versions of Comfy UI, run the GIT pull command in the command window and you'll be able to load this bunch of commands. Especially, you'll see this one file called compile VAE. That means this is a new file that supports 1 2.2, indicating that your Comfy UI is successfully updated to support 1 2.2.

[04:47] Now, come to the Comfy UI official page. There are a few examples you can check out. I won't go through them too much, like reading those text prompts for you. It doesn't really make sense for my video to read text prompts for you. Anyway, we're moving on to the practical stuff. How do we get it done in the Comfy UI repackaged repo for 1 2.2? Once you click in here, go to the file versions, then the split files, and you'll see the diffusion models folder, the text encoder, and the VAE folder. The VAE folder is the first thing I'm going to mention. They've also included the one 2.1 VAE for 1 2.2. Don't delete the 1 2.1 VAE just because you think, oh, we have 1 2.2 already so we don't need the 2.1 version. No, you still need it, and you'll see why later.

[05:37] Now going back to the text encoder, if you're an existing user of 1 2.1, you don't need to download additional things for the text encoder because the UMT 5 XXL text encoder remains the same. I'm going to use FP16, whichever you prefer, but I'll stick with FP16 for the text encoder. Go to the split files and now we're looking at the diffusion model. The diffusion model here is something unusual compared to other AI models that only have one single safe tensor file. Here, we've got one 2.2 image-to-video, and then below it, a list for text-to-video. This tool includes the FP16 and FP8 versions of each text-to-video and image-to-video model. And each of those, for the 14 billion parameter models, has something called the high noise and low noise model. You'll need to download both if you want to run the 14B models locally.

[06:33] Right here, as you can see, this is a pair of models you'll need if you run FP16. Just like in my case, I downloaded the image-to-video 14B model in FP16. So, I have the low noise model and I also need to download the high noise model as a pair. And that doubles your file storage, which isn't really convenient for most consumer PCs. Because when you see that, when I download the FP16, I'm using 28 gigabytes for one file. And since this is a pair of FP16 one 2.2 models, that means you're looking at around 50 gigabytes of file storage. By downloading these two models, including some cache and other things, running FP16 with the 14 billion parameter model is going to require about 60 gigabytes of VRAM to temporarily store the models unloaded in your local GPU. So, it's not ideal for most people to use. This is what I was talking about earlier in the video. Even the FP8 models take about 14 gigabytes of file storage for a single file. And including the low noise adds another 14 gigabytes, which means you're going to need about 30 gigabytes of file storage and about 30 gigabytes of VRAM when you execute this FP8 model.

[07:48] The more convenient way is the hybrid model with 5 billion parameters. They did a really good job because even though this is a smaller parameter size, they used FP16 for folding points of this model, getting pretty decent quality even at this small 5B parameter size. This only requires 10 gigabytes of file storage, which most modern consumer PCs with Nvidia GPUs nowadays can run without a problem.

[08:15] If you still want to run the 14B models for image-to-video or text-to-video but don't have that much VRAM in your GPU, there's an alternative way: the GGUF quantization model. Again, you'll need both the high noise and low noise models in pairs. For example, let's say we have the Q8 at the bottom here. This is the 1 2.2 I2V low noise 14B Q8, the 8-bit quantized model size, which still requires 15 gigabytes of file storage. So if you download this one, you'll still need to download the high noise version of this model, which is the one I'm highlighting: image-to-video high noise 14B Q8. You'll need to download this pair of files for execution.

[08:58] Now, let's go to Comfy UI. After you update your Comfy UI, you can start with the new workflow here. As you can see, I just tested two combinations. One is the normal runtime generating this model, this video, and the other one, which I connected, is using Sage attention to generate this video. Both qualities are pretty similar.

[09:19] So, how do you get this workflow? First, when you update your Comfy UI, you can go to the browse templates. Nowadays, they have a lot of predefined workflows thanks to the Comfy UI development team. You can click the video tab, and there you have it. You'll find three one 2.2 workflows available at this moment. There's the 14B model for text-to-video and image-to-video, and also the 2.2 hybrid model called the 5B video generation model. Either one can run the one 2.2 model, but you'll need to measure your GPU to see if it can handle the 14B model. If you're running on a low VRAM consumer PC, I suggest the 5B model. And the 5B model isn't really low quality. It's pretty decent, especially for a 5 billion parameter model.

[10:09] In this workflow, I'm showing here currently, this is the 5 billion parameter model. We're using the same good old UMT 5 XXL text encoder. Pay attention to the load VAE here because this is something different. When using the 5 billion parameter hybrid model, we're using the one 2.2 VAE, which they mentioned in their GitHub repo. They trained these hybrid models and used the one 2.2 VAE for training the hybrid text-to-image-to-video model. So remember, you have to download this if you run the hybrid model.

[10:44] Now, when loading this, it's pretty simple for the K sampler. Just like usual, we're using the uni PC scheduler, a very basic way to generate a video. We use step 20 as a test for the first time we load this workflow template, CFG 5, and shift 8, which are the default values in this template. The only thing I've changed is adding the sage attention node here. I just wanted to see if there's any difference.

[11:09] Underneath here, once we see the latent image, if we're using the hybrid model like this one, the text-to-video, the only thing we need to do is disable the load image node. As you can see, this is a new node called the one 2.2 image-to-video latent. Think of it like a switch. If you bypass the load image node here, it means we don't have an image as input and it will automatically switch this latent node to an empty latent, making it a text-to-video workflow.

[11:38] In this case, if you turn the load image on and input an image here, setting the width and height correctly, it becomes an image-to-video workflow. Let's say I have my previously generated videos here before recording this YouTube video. I tested two different variants. By default, the text prompts for loading this workflow template in Comfy UI are very similar. As you can see, the compositions of the guitar player in the subway station are standing in a similar direction. There's also a speaker behind the guitar player, and the same composition is here as well. But for sage attention, as you can see, it gets less detail on the face. Check this part here, and especially the audience behind, someone is covering the camera here. They're not really detailed on the face.

[12:26] Moving on to another example, as you can see in this variant, I'm not using sage attention and just purely running the 5 billion parameter model. It's pretty impressive for such a small model. Remember, last year we used cog video X, which is also a 5 billion parameter model. Comparing the video quality of that with one 2.2 right now, it's a totally different story. So, just by measuring the size of this model as a 5 billion parameter model, you can see it's quite impressive already for the quality. You get pretty good details on this speaker, and there are two people having a romantic moment behind the guitar player.

[13:04] Anyway, we're moving on to the next thing, the 14 billion parameter model. Now, the 14B model here, first, I loaded the image-to-video workflow the same way I found it in the browse templates. Then, you go to the video tab. Once you're in the video tab, you'll see the one 2.2 14B models for text or for image. Here, I've used the image-to-video model only, and I only downloaded the 14B model for image-to-video because that's good enough for what I needed to do.

[13:36] Moving on here, as you can see, there are two diffusion models loaded. The one on top is the high noise for the 14B model, and the one below is the low noise 14B model. The way the mixture of experts works is that once we have the high noise model, we bring all this data to the first case sampler advanced. If you've played around with image generation models, you'll know this node well for sampling. The steps here can be customized. For example, the start step is at zero and the end step is at 10. That means this case sampler advanced will run 10 steps within the total of 20 steps, meaning the first case sampler runs 50% of the sampling for this AI using the high noise model.

[14:18] Then, we have the low noise model, which brings all this data again into another model sampling process. It goes to the lower part of this workflow, which is another case sampler advanced. This case sampler advanced takes the previous case sampler's returned noise. You have to enable that in the first case sampler advanced to return whatever noise is left over, and also adds noise in the first case sampler. So you have the enabled options here to see once you have the enabled options going on, and it will bring the latent image data, which is this case sampler. This case sampler is running the low noise model, and as you can see, it's using add noise disabled and return leftover noise, also disabled because you don't have extra steps going on in this workflow again. So, it doesn't need to return leftover noise, and here it will get the final latent data as output to your VAE decode. And look at this beautiful girl walking toward the camera. This is what I just generated using the 14B model right here.

[15:20] Focusing more on this part, this is an interesting thing because when you use the mixture of experts in language models, it's kind of a similar concept to this video diffusion model. When you have the second step here, there's no noise, no additional things required. This sampler just adds this latent data into your video, using only the leftover steps. For example, we have a total of 20 steps. The start step here is starting at 10 and running to the end, which is set here as 10,000, but you can set this to 20 if your maximum steps are 20. For safety, we often set really high numbers here, just to be sure. We focus on the number of steps in this part, the 20 steps here.

[16:04] Anyway, coming back to the overview of this workflow, this is going to need two models. This is what I talked about earlier in the video. We have to download these two files as a pair for your 14B video generation. Then, moving down to the load VAE and text encoder, as you can see, the text encoder remains the same. The load VAE is different between the 5 billion parameter model and the 14B model. Funny enough, for the 14B model, we're using the WAN 2.1 VAE. The first time I tried to use the WAN 2.2 VAE in this workflow, it returned an error, something about different channels, 64 or something. That means it was returning the wrong diffusion model for the execution of the AI.

[16:54] So we're using the one 2.1 VAE with the 14B mixture of experts model. Here, as you can see, it's very clear. 2.1 image-to-video node here to connect the conditioning and the start image, something we don't need to use if you pay attention here. We don't need the clip vision in the new one 2.2. See, this is clearer and has fewer custom nodes connecting around because we don't need clip vision in this case, which brings you more convenience in some ways for running this model.

[17:25] Also, in the 5B model, something you might notice is that we don't need vision either. So, both versions of the one 2.2 models require less setup, but the 14B model really requires a large amount of VRAM to run. Because when I ran this model in FP16, it loaded 61 gigabytes of VRAM because my GPU is large enough to store the full size of this model. So, it just puts everything into the GPU VRAM at once. I heard someone using an Nvidia 5090, they said that Comfy UI won't load everything at the same time. Instead, it first runs the high noise model, unloads it, then starts loading the low noise model in sequence.

[18:09] I'm not sure if that's the way this model is supposed to work, but in my situation, because once Comfy UI detected my GPU had enough space, it just put everything into the GPU VRAM already. But you can see that the quality of the 14B model, especially for image-to-video, is pretty nice. You don't see any morphing, broken hands, or funky parts happening with the character or the background. I've used this image before in Minimax videos for testing and other AI video models. I've used this image as a demo test before, and none of them were able to create smooth hands like a fashion model walking forward toward the camera. Most of the time, other AI video models create slow-motion scenes of the character walking toward the camera or just a simple camera pan. But in this case, it's really good in prompt adherence, especially since I just used a very loose, low-quality text prompt. I didn't try to use a vision language model to make a long essay of a text prompt.

[19:08] So, this is really cool to play around with the 14B model. For GGUF users, if you still want to use the 14B model and install GGUF to run one 2.2, another way to load this with GGUF is to still use this template. Once you have this node here, what you'll do is replace these connections with the GGUF model loader. Let's say I'm using the simple unet loader for GGUF, and because I haven't downloaded any GGUF files currently for one 2.2, I only have this 1 2.1 base for testing and demo purposes. But let's say you've downloaded both the high noise and low noise Q8 models, then you would create two unet loader GGUF nodes. One is for the high noise, connecting it like this, and the second one replaces the connection for the low noise diffusion model. So, in this way, we're going to connect another one, the unet loader GGUF to the model sampler SD3 node here and send that data to the K sampler. But again, I don't have the GGUF downloaded and I don't need it on my computer anyway. So this is just for demo purposes, this way of connecting to replace the load diffusion node so you can use GGUF to run the 14B model as well.

[20:26] A lot of things have changed compared to 1 2.1 if you're running the 14B model. The most convenient way, surprisingly, is the 5 billion parameter model. Although it's a small size model, it's worth trying. It's worth it for everyone. Even if you have low VRAM, just 16 or 12 gigabytes, you can still run this because it only takes about 10 gigabytes of file storage. When loaded into VRAM, it's almost 10 gigabytes or so. The quality here isn't really bad. And I'm going to try another text prompt instead of this guitar player in the subway station.

[21:00] Here, I have my previous text prompt that I've been testing for Movie Gen, which generated this video in 1 2.1 Movie Gen. Using the same text prompt here, I'll try with higher sampling steps. I want to go for 30 sampling steps here and see what we get. I'll also use 720p resolution. Actually, in 1 2.2, one thing worth mentioning is that the width and height are a little different. In 1 2.1, if we used 720p for the height, that was straightforward. But here, once we set 720p, it automatically changes for you to 736. This is the one we should choose to correspond with the 1,280 pixel width. These two combinations should be the 720p resolution you want to choose in 1 2.2. So, let's check this text prompt, see how fast it runs and how the quality is.

[21:49] We used 3 minutes and 16 seconds for 30 sampling steps without any sage attention or torch compile or whatever methodologies you're trying to make it faster. None of that, just a pure native node generation here. Even though I boosted the sampling steps to 30, previously, I used 20 steps and it took 1 minute and 11 seconds. But don't take my measurement here as the standard because again, different GPUs, different power, different chips, and load up speeds are different. So, you'll need to try it yourself.

[22:20] And here's the example demo I generated using the same prompt. Although the seed numbers might not be lucky this time, not really nice on the motion, you can see that it understands my prompts really well throughout the entire motion compared to what I have here. This video was generated using Movie Gen in 1 2.1. Although this one is pretty cool, you see the fast speed motions. When you look at the motorbike and the character, they're not detailed enough in some ways. It hasn't been upscaled. This video clip is just raw output from Comfy UI. I like to see the raw output because that's how the AI actually performs rather than giving you the beautiful side of things after upscaling and adding detail. So, this one is actually more detailed, I would say, in 1 2.2. When you see the motion of the car turning the corner from here, the motorbike is kind of leaning to the left side rather than being completely straight. You don't feel like the bike is turning left or right, but actually, the roll here shows it's going to the right side like this. It's not really, if we have to be picky and deal with all the physics stuff in the video clip, 1 2.2 is actually getting better physics. You see that here because it's turning the corner, and in common sense, people know that turning a corner on a motorbike means you should lean on either side. And this looks pretty cool, but only in this part does it not look well.

[23:48] Now, I've run two more of the same text prompts for this motorcycle text prompt, where I've tried different seed numbers and sampling steps as well. Basically, the 30 sampling steps from here, and this one is 20 sampling steps throughout the display here. Well, obviously, the 20 sampling steps give you less detail on the biker, the character itself. The first assembling step gives you a clearer view of the leather jacket and how it's displayed in a fast motion scene. Even in a fast motion scene, you see those neon lights and some futuristic city details going on here. Now, this is generated in a 5 billion parameter model. My previous examples generated here using Movie Gen are 14 billion parameter models in 1 2.1. Even though I'm not comparing the same size of AI models, it's still able to get something very close to the quality of a 14B in 1 2.1 when I'm using the 1 2.2 5B model. So, this model, the hybrid 5B model, is really worth trying for consumer PCs. It's really fun to play around with. It feels like LTX where you have one model able to generate text-to-video and image-to-video as well. The quality here is obviously way better than what we just saw in LTX 13B. And again, this is in the 5 billion parameter model size.

[25:09] Here, I've done another experiment using this AI image that I generated before. This time, I set it to 720p and used just 20 steps here. Other examples I've tried before are in 480p. So, 480p is obviously kind of blurry for the face and pixelated on the eyes, just like in 1 2.1. Exactly the same thing happened back then in 1 2.1 as well. So, I suggest that if you really want to do detailed work on the character's face or objects that need more detail from the reference, you might need to use 720p resolution. That will get you a lot more detail, and the motion as well. When you use 720p, it's going to look more natural. As you can see, both are walking in the same direction. So, 480p is, it's kind of walking too fast and too jumpy for the character. Some people like jumpy, bouncy movements, but if I really need to make this for work, like for fashion videos or something, you can't just have the woman jumping and bouncing like that, right? Yeah, so looking more natural, 720p is more natural in this case for video generation. For the timing of generation, it doesn't make too much difference. I just changed the resolution here. The previous one was 480p, which took 43 seconds, and this time, 720p took 1 minute and 12 seconds. Again, my GPU can't be the standard answer for all of you. You have to measure it with whatever GPU you have. But in this case, as a test experiment, I don't see too much difference in timing with the 5B model. I'd rather wait and generate one good quality video. That's the strategy I would go for if I'm using the 5B model. So, let's try the same image because I have something similar to this image, and I'll use the same text prompt and settings, going with the 14B model. This big boy needs something to run as well.

[27:07] As you can see, this pink dot connects to the second stage of the workflow using the low noise model here and finishing off the rest of the sampling steps in this part. So, it's going to take a while, and you'll need to be patient if you're running this model. Even in FP8 for the 14B model, it's pretty heavy. It's not crazy heavy like freezing your computer where you can't do anything, but it is consuming a lot of VRAM to be honest. You have to prepare before you run this.

[27:35] Let's see my current runtime and GPU usage. So, in the task manager, as you can see here, I have my GPU usage. First, loading the width together with the high noise model and the low noise model consumed about 52 gigabytes of VRAM already. I noticed that, and other Patreon members have mentioned that once we finish the first sampling using the high noise, it will unload the high noise model and remain with about 30-something gigabytes of VRAM in my graphics card to continue with the low noise model. That means that at the first moment, because my GPU has enough space to store both models, it will put these two models together into my VRAM. Once it finishes the first sampler, it will unload and continue with the low noise model, remaining with about 30-something gigabytes of VRAM to finish off the video generation.

[28:27] So, I just used the 14B model and generated an image-to-video clip. I was trying to do some experiments, and a funny thing is that when I switch this width and height back to 480p resolution, the generation times here were using 3 minutes for the first sampling and another 3 minutes for the second sampling, which is back to the normal 1 2.1 time. Back then, we were using 6 or 7 minutes for 1 2.1 480p. It's something fun to play around with when we can use a smaller resolution. You know, if you have an idea proof of concept or want to make a prototype of your video first, you can use this with 1 2.2 where you see the motions here. It's way better than the previous ones we generated in the 5B model. Of course, you'll see more motion from the characters, like the hands holding on the hips and doing more modeling poses like that within a very short duration.

[29:22] Anyway, I'll try another image that's going to have better quality by using 720p in the next round here. So, I'm going to set this back to 720p resolution and choose another image for this generation.

[29:35] As you can see this time, the motion is way better than 1 2.1, obviously. The car overall as an object doesn't break, and the acceleration is way better going in one direction this time. As you can see here, I just used one-time generation for this image-to-video. I didn't generate multiple times and cherry-pick the good one to show you guys. I expect it should have some issues with vehicles going in the wrong direction because back then, in 1 2.1, when I tried images like this, sometimes the car would go the other side of the road or turn backward and drive backward. But this time, you see all the shadows of the trees and vehicle shadows following the physics and the real world of sunlight here.

[30:17] One thing worth mentioning is that these models have been trained on lighting. As you can see in the beginning of the intro video, they put effort into making the lighting and object shadows even better. You can see some physics are getting more realistic here. Yeah, so the 14B model is obviously way better than the 5B model, and even the 14B compared to 1 2.1's 14B is a lot better in all performance factors, benchmark numbers and such. It's just better than what they had in 2.1.

[30:49] So there you go. You have 1 2.2 and it's ready to play around with. Download it and we're going to explore a lot more in upcoming videos. I'm talking about a lot of video tutorials we can go through because we're just in the first day of 1 2.2 release. This is just the beginning of this AI. So, I'll see you guys soon. Have a nice day. See ya.

---
# TAXONOMY ANALYSIS

## 4. Workflows Identification

### WORKFLOW 1: Text-to-Video Generation (5B Hybrid Model)
- **OBJECTIVE**: To generate a video from a text prompt using the more resource-efficient 5-billion parameter hybrid model.
- **STEPS**:
  1. Update `ComfyUI` to the latest version.
  2. Load the predefined `Wan 2.2 5B Video Generator` template.
  3. Load the `wan2_2wan2.2_i2v_5B_fp16.safetensors` diffusion model.
  4. Load the `umt5_xxl_fp16.safetensors` CLIP model.
  5. Load the `wan2.2_vae.safetensors` VAE model.
  6. Disable or bypass the "Load Image" node to switch the `Wan22ImageToVideoLatent` node into text-to-video mode.
  7. Enter a positive and negative text prompt into the `CLIP Text Encode` nodes.
  8. Configure sampler settings (e.g., 30 steps, `uni_pc` sampler).
  9. Execute the workflow to generate the video.
- **TOOLS USED**: `ComfyUI`, `Wan 2.2 (5B Hybrid Model)`
- **INPUT**: Text prompt.
- **OUTPUT**: MP4 video file.

### WORKFLOW 2: Image-to-Video Generation (14B MoE Model)
- **OBJECTIVE**: To generate a video from a starting image using the high-quality 14-billion parameter Mixture of Experts (MoE) model.
- **STEPS**:
  1. Load the `Wan 2.2 14B Image to Video` template in `ComfyUI`.
  2. Load the "high noise" diffusion model (e.g., `wan2_2wan2.2_i2v_high_noise_14B_fp16.safetensors`).
  3. Load the "low noise" diffusion model (e.g., `wan2_2wan2.2_i2v_low_noise_14B_fp16.safetensors`).
  4. Load the `umt5_xxl_fp16.safetensors` CLIP model.
  5. Load the `wan_2.1_vae.safetensors` VAE model (Note: uses the older VAE).
  6. Upload a start image in the "Load Image" node.
  7. Enter positive and negative text prompts.
  8. The workflow uses a two-stage sampling process:
     a. The first `KSampler (Advanced)` runs for the initial steps (e.g., 0 to 10) using the high-noise model and passes the leftover noise.
     b. The second `KSampler (Advanced)` takes the latent from the first and continues sampling for the remaining steps (e.g., 10 to 20) using the low-noise model.
  9. The final latent is decoded by the VAE.
  10. Execute the workflow to generate the final video.
- **COMPLEXITY**: High (due to two-stage sampling and high VRAM requirements).
- **TOOLS USED**: `ComfyUI`, `Wan 2.2 (14B MoE Models)`
- **INPUT**: Start image and text prompt.
- **OUTPUT**: MP4 video file.

### WORKFLOW 3: Model Installation and Setup
- **OBJECTIVE**: To download and set up the necessary Wan 2.2 models for use in ComfyUI.
- **STEPS**:
  1. Navigate to the Wan AI page on Hugging Face.
  2. Go to the "Files and versions" tab.
  3. Select the desired model files (e.g., 5B hybrid, 14B MoE high/low noise pairs, VAEs, CLIP model).
  4. Download the `.safetensors` files.
  5. Place the downloaded models into the appropriate directories within the `ComfyUI` installation folder.
- **TOOLS USED**: `Hugging Face`, `ComfyUI`
- **INPUT**: Model repository URL.
- **OUTPUT**: Locally stored AI model files ready for use.

## 5. Action Verbs & Operations

#### A. CREATION VERBS
- Generate
- Create

#### B. MODIFICATION VERBS
- Change
- Adjust
- Update
- Customize
- Set
- Replace

#### C. ANALYSIS VERBS
- Check out
- Judge
- Measure
- Compare
- Test

#### D. ORGANIZATION VERBS
- List

#### E. COMMUNICATION VERBS
- Show
- Mention
- Explain

#### F. BROWSER/AGENTIC OPERATIONS
- Go to
- Click
- Scroll down
- Navigate

#### G. DATA OPERATIONS
- Download
- Load
- Unload
- Upload
- Input
- Output
- Store
- Train
- Quantize
- Connect
- Bypass
- Execute
- Run

## 6. Task Chains

- **TASK CHAIN**: 14B MoE Video Generation
  Load high-noise model → First KSampler (initial steps) → Return leftover noise → Load low-noise model → Second KSampler (remaining steps) → VAE Decode → Final Video

- **TASK CHAIN**: Hybrid Model Text-to-Video Generation
  Disable Image Input → `Wan22ImageToVideoLatent` node creates empty latent → KSampler generates video from text prompt → VAE Decode → Final Video

- **TASK CHAIN**: Hybrid Model Image-to-Video Generation
  Load Image → `Wan22ImageToVideoLatent` node uses image as start latent → KSampler generates video from image + prompt → VAE Decode → Final Video

## 7. Responsibilities Vocabulary

#### Professional Roles Mentioned:
- AI User
- Developer
- Patreon Members

#### Responsibilities/Activities:
- "run your AI video generation" [00:54]
- "training AI models" [02:33]
- "generating this model" [09:08]
- "running the 14B model" [13:10]
- "doing some experiments" [28:33]

#### Skills Mentioned:
- [None explicitly mentioned]

## 8. Tools & Technologies Matrix

| Tool Name | Category | Purpose | Used For | Mentioned With |
|---|---|---|---|---|
| `Wan 2.2` | AI Video Model | Open-source video generation from text or images. | Creating videos with controls for lighting, camera, saturation. | `Hugging Face`, `ComfyUI` |
| `Hugging Face` | Model Hub | Hosting and distributing AI models. | Downloading the Wan 2.2 models. | `ModelScope`, `GitHub` |
| `ModelScope` | Model Hub | Alternative platform for hosting AI models. | Releasing the Wan 2.2 model. | `Hugging Face` |
| `ComfyUI` | AI Interface | Node-based graphical user interface for running AI models. | Running Wan 2.2 workflows in a user-friendly way. | `Diffusers`, `Python` |
| `GitHub` | Code Repository | Hosting the source code for the Wan 2.2 project. | Checking the project details and license. | `Apache 2.0 License` |
| `Diffusers` | Library | A Hugging Face library for running diffusion models. | Programmatic video generation with Wan 2.2. | `Python`, `ComfyUI` |
| `Python` | Programming Language | Scripting language for running AI models. | Running Wan 2.2 programmatically. | `Diffusers` |
| `MovieGen` | AI Video Model | A previous version or related model used for comparison. | Generating a baseline video to compare against Wan 2.2. | `Wan 2.1` |
| `GGUF` | Model Format | A quantized model format for running large models on lower VRAM. | An alternative way to run the 14B models on consumer GPUs. | `ComfyUI` |

## 9. Objects & Deliverables

- AI-generated videos (MP4)
- 720p resolution videos
- 480p resolution videos
- Raw video output (pre-upscaling)
- Latent images
- Predefined ComfyUI workflow templates

## 10. Integration Patterns

- **INTEGRATION**: `Wan 2.2 Models` + `ComfyUI`
  - **PURPOSE**: To provide a user-friendly, node-based interface for generating videos with the Wan 2.2 models.
  - **FLOW**: `Wan 2.2 model files` → are loaded into → `ComfyUI nodes` (Load Diffusion Model, Load VAE, etc.) → to execute a generation workflow.

- **INTEGRATION**: `High-Noise Model` + `Low-Noise Model` (14B MoE)
  - **PURPOSE**: A two-stage sampling process to generate high-quality video, leveraging the Mixture of Experts (MoE) architecture.
  - **FLOW**: `High-Noise Model output (latent + leftover noise)` → becomes → `Low-Noise Model input` → for final sampling steps.

- **INTEGRATION**: `Wan 2.2` + `Diffusers`
  - **PURPOSE**: To enable programmatic, code-based generation of videos using the Wan 2.2 models.
  - **FLOW**: `Python script` → calls → `Diffusers library functions` → which load and run the → `Wan 2.2 models`.

## 11. Business Concepts & Strategy

- **Open Source Model**: Wan 2.2 is released under the **Apache 2.0 license**, which allows for both private and **commercial use** [01:12].
- **Cost-Effectiveness (MoE)**: The Mixture of Experts (MoE) architecture is described as more "cost-efficient" because it doesn't load every single parameter during execution, making large models more manageable [02:49].
- **Hardware Tiering**: The video highlights different models for different hardware capabilities. The **5B hybrid model** is recommended for most consumer PCs with lower VRAM, while the **14B MoE models** are for high-end systems with significant VRAM (60GB+ for FP16) [04:01].
- **Prototyping**: The creator suggests using smaller resolutions (like 480p) to create a **proof of concept** or prototype of a video quickly before committing to a longer, higher-resolution render [29:00].

## 12. Optimization & Best Practices

- **OPTIMIZATION**: VRAM Management for 14B Models
  - **TECHNIQUE**: Use the GGUF quantized versions of the 14B models if your GPU has insufficient VRAM for the full FP16/FP8 versions.
  - **REASON**: GGUF reduces the model size and VRAM footprint, making it runnable on consumer-grade hardware, though it still requires significant resources (~30GB VRAM).
  - **EVIDENCE**: [08:15 - 08:42]

- **OPTIMIZATION**: Workflow for Different Hardware
  - **TECHNIQUE**: For GPUs with low VRAM (12-16GB), use the 5B hybrid model. For high-end GPUs (60GB+), use the 14B MoE models.
  - **REASON**: Matches the model's resource requirements to the available hardware to prevent errors and ensure successful generation.
  - **EVIDENCE**: [04:01 - 04:09]

- **OPTIMIZATION**: Model File Management
  - **TECHNIQUE**: When using the 14B MoE models, you must download both the "high_noise" and "low_noise" models as a pair.
  - **REASON**: The workflow is a two-stage process that requires both models to function correctly.
  - **EVIDENCE**: [06:24 - 06:33]

- **OPTIMIZATION**: Correct VAE Usage
  - **TECHNIQUE**: The 5B hybrid model uses the new `wan2.2_vae.safetensors`, while the 14B MoE models require the older `wan_2.1_vae.safetensors`.
  - **REASON**: Using the wrong VAE will result in an error. The models were trained with specific VAEs.
  - **EVIDENCE**: [10:19, 16:34]