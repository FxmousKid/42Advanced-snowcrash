# SnowCrash

Run the VM with QEMU, then SSH into it. That's it.

## 1. Install QEMU (once)

```sh
brew install qemu
```

## 2. Start the VM

From this folder (where `SnowCrash.iso` is):

```sh
qemu-system-x86_64 -m 2G -cdrom SnowCrash.iso -nic user,hostfwd=tcp::4242-:4242
```

A QEMU window opens. Wait for the `SnowCrash login:` prompt. Don't type in it, just leave it open.

## 3. SSH into it

Open a second terminal:

```sh
ssh -p 4242 level00@localhost
```

Password: `level00`

You're in. Follow the subject from there (`su flag00`, `getflag`, etc.).

## 4. Stop the VM

Close the QEMU window, or `Ctrl+C` in the terminal that started it.

## Copying files out of the VM

```sh
scp -P 4242 level00@localhost:/path/to/file .
```

## Why `localhost` and not the IP shown on screen?

The VM shows `10.0.2.15`. That's QEMU's private network, your Mac can't reach it directly.
The `hostfwd=tcp::4242-:4242` part forwards your Mac's port 4242 to the VM's port 4242, so `localhost:4242` = the VM.
