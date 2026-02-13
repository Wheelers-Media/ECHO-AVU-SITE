"use client";

import { useRef } from "react";
import { useInView } from "framer-motion";

// Simple utility 
function classNames(...classes: (string | undefined | null | false)[]) {
    return classes.filter(Boolean).join(" ");
}

interface ScrollSpotlightProps extends React.HTMLAttributes<HTMLDivElement> {
    children: React.ReactNode;
    className?: string; // Base classes
    activeClassName?: string; // Applied when in "Hot Zone" (Mobile)
    inactiveClassName?: string; // Applied when NOT in "Hot Zone" (Mobile)
}

export default function ScrollSpotlight({
    children,
    className,
    activeClassName = "max-md:border-signal/50 max-md:grayscale-0 max-md:opacity-100", // Default Active Defaults
    inactiveClassName = "max-md:border-white/10 max-md:grayscale max-md:opacity-50", // Default Inactive Defaults
    ...props
}: ScrollSpotlightProps) {
    const ref = useRef<HTMLDivElement>(null);

    // "Hot Zone" = Middle 40% of the screen (-30% top, -30% bottom)
    const isInView = useInView(ref, {
        margin: "-30% 0px -30% 0px",
        once: false
    });

    return (
        <div
            ref={ref}
            className={classNames(
                // Base Class (Always Applied)
                className,

                // MOBILE LOGIC (< md)
                // Note: We use `max-md:` prefix to Ensure this logic ONLY touches mobile.
                // On desktop (md+), these classes are ignored, letting :hover take over.

                isInView
                    ? (activeClassName || "")
                    : (inactiveClassName || "")
            )}
            {...props}
        >
            {children}
        </div>
    );
}
