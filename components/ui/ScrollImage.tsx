"use client";

import { useRef } from "react";
import Image, { ImageProps } from "next/image";
import { useInView } from "framer-motion";
// Simple utility since we are self-contained here
function classNames(...classes: (string | undefined | null | false)[]) {
    return classes.filter(Boolean).join(" ");
}

interface ScrollImageProps extends ImageProps {
    containerClassName?: string;
}

export default function ScrollImage({
    src,
    alt,
    className,
    containerClassName,
    ...props
}: ScrollImageProps) {
    const ref = useRef<HTMLDivElement>(null);

    // "Hot Zone" = Middle 40% of the screen (-30% top, -30% bottom)
    const isInView = useInView(ref, {
        margin: "-30% 0px -30% 0px",
        once: false
    });

    return (
        <div
            ref={ref}
            className={classNames("relative overflow-hidden w-full h-full", containerClassName)}
        >
            <Image
                src={src}
                alt={alt}
                className={classNames(
                    // Base transition
                    "transition-all duration-700 ease-out",

                    // Desktop Behavior (md+):
                    // Default: Grayscale, Scale 100
                    // Hover: Color, Scale 1.02
                    "md:grayscale md:scale-100 md:hover:grayscale-0 md:hover:scale-[1.02]",

                    // Mobile Behavior (max-md):
                    // We use the `isInView` state to toggle classes specifically for mobile
                    // On desktop, we rely on the group-hover logic defined in parent or default state
                    isInView
                        ? "max-md:grayscale-0 max-md:scale-[1.02]" // Active (In Center)
                        : "max-md:grayscale max-md:scale-100",    // Inactive

                    className
                )}
                {...props}
            />
        </div>
    );
}
